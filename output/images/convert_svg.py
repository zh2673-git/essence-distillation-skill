import os, glob, re, base64

os.chdir(r'd:\self_test\project\SKILL\custom\本质蒸馏\output\images')
svgs = sorted(glob.glob('0*.svg'))

try:
    from playwright.sync_api import sync_playwright
    print("Using Playwright for SVG->PNG conversion...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for svg_file in svgs:
            png_file = svg_file.replace('.svg', '.png')
            with open(svg_file, 'r', encoding='utf-8') as f:
                svg_content = f.read()
            m = re.search(r'width="(\d+)".*?height="(\d+)"', svg_content)
            w, h = int(m.group(1)), int(m.group(2))
            page = browser.new_page(viewport={'width': w, 'height': h}, device_scale_factor=2)
            svg_b64 = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
            page.goto(f'data:image/svg+xml;base64,{svg_b64}', timeout=60000)
            page.wait_for_timeout(500)
            page.screenshot(path=png_file, timeout=60000)
            page.close()
            print(f"  Converted: {svg_file} -> {png_file}")
        browser.close()
    print("All SVGs converted to PNG successfully!")
except ImportError:
    import cairosvg
    print("WARNING: Playwright not available, falling back to cairosvg...")
    for svg_file in svgs:
        png_file = svg_file.replace('.svg', '.png')
        cairosvg.svg2png(url=svg_file, write_to=png_file, scale=3)
        print(f"  Converted: {svg_file} -> {png_file}")
    print("Done (Chinese fonts may render incorrectly with cairosvg).")
