from flask import Blueprint, render_template
from sqlalchemy import select
from app.models import PesananProduk
from database import Session

pesanan_blueprint = Blueprint('pesanan_blueprint',__name__)

@pesanan_blueprint('/pesanan/lihat_lama_produksi/')
def lihat_lama_produksi():
    session = Session()

    daftar_pesanan = session.execute(
        select(PesananProduk.kode_pesanan, PesananProduk.).outerjoin()
    )

    return render_template('templates/lihat_lama_produksi.html',daftar_pesanan)

