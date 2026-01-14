import base64
import io

import qrcode
from django.shortcuts import render


def index(request):
    context = {}
    if request.method == "POST":
        data = request.POST.get("qr_text")
        if data:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            qr_base64 = base64.b64encode(buffer.getvalue()).decode()
            context['qr_code'] = qr_base64
            context['original_text'] = data
    return render(request, "generator/index.html", context)
