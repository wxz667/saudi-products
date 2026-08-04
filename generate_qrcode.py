"""
QR码生成脚本
用法: python generate_qrcode.py "https://你的网址/"
会在当前目录生成 qrcode.png
"""
import sys
import qrcode

def generate(url, output="qrcode.png"):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # 15%容错
        box_size=12,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output)
    print(f"QR code saved: {output}")
    print(f"URL: {url}")
    print(f"Size: {img.size}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("请输入网址: ").strip()
    if not url.startswith("http"):
        url = "https://" + url
    generate(url)
