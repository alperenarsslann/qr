from __future__ import annotations

import argparse
from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_M


DEFAULT_URL = "https://alperenarsslann.github.io/qr/"
DEFAULT_OUTPUT = "portfolio_qr.png"


def build_qr(data: str, output: Path, box_size: int, border: int) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(output)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a QR code PNG for the portfolio page or custom text."
    )
    parser.add_argument(
        "data",
        nargs="?",
        default=DEFAULT_URL,
        help=f"Text or URL to encode. Defaults to {DEFAULT_URL}",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=DEFAULT_OUTPUT,
        help=f"Output PNG path. Defaults to {DEFAULT_OUTPUT}",
    )
    parser.add_argument(
        "--box-size",
        type=int,
        default=10,
        help="Pixel size of each QR module. Defaults to 10.",
    )
    parser.add_argument(
        "--border",
        type=int,
        default=4,
        help="Quiet-zone border width in QR modules. Defaults to 4.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = Path(args.output)
    build_qr(args.data, output, args.box_size, args.border)
    print(f"QR code written to {output.resolve()}")


if __name__ == "__main__":
    main()
