from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, LargeBinary, Boolean, Table
from sqlalchemy.orm import relationship
from database import Base


class Customer(Base):
    __tablename__ = 'customer'

    nik = Column('nik', String(16), primary_key=True)
    nama = Column('nama', String(100), nullable=False)
    alamat = Column('alamat', String(100), nullable=False)

    pesanan = relationship('Pesanan', backref='customer ', cascade='save-update')


class Pesanan(Base):
    __tablename__ = 'pesanan'

    kode_pesanan = Column('kode_pesanan', String(16), primary_key=True)
    nik = Column('nik', String(16), ForeignKey('customer.nik'), primary_key=True)
    tanggal_pesanan = Column('tanggal_pesanan', DateTime(timezone=True))
    estimasi = Column('estimasi', Integer)

    customer = relationship('Customer')
    pesanan_produk = relationship('PesananProduk', backref='pesanan_produk', cascade='save-update')
    karyawan_handle_pesanan = relationship('KaryawanHandlePesanan', backref='kode_pesanan', cascade='delete')


class PesananProduk(Base):
    __tablename__ = 'pesanan_produk'

    kode_pesanan = Column('kode_pesanan', String(16), ForeignKey('pesanan.kode_pesanan'), primary_key=True)
    kode_produk = Column('kode_produk', String(16), ForeignKey('produk.kode_produk'), primary_key=True)
    quantity = Column('quantity', String(100), nullable=False)
    tanggal_mulai_produksi = Column('tanggal_mulai_produksi', DateTime(timezone=True), nullable=False)
    tanggal_selesai_produksi = Column('tanggal_selesai_produksi', DateTime(timezone=True), nullable=False)
    subtotal_harga = Column('subtotal_harga', Float(100), nullable=False)
    penilaian = Column('penilaian', String(100))

    pesanan = relationship('Pesanan')
    produk = relationship('Produk', backref='pesanan_produk')


class Produk(Base):
    __tablename__ = 'produk'

    kode_produk = Column('kode_pesanan', String(16), primary_key=True)
    nama_produk = Column('nama_produk', String(100), nullable=False)
    harga_satuan = Column('harga_produk', String(100), nullable=False)
    foto_produk = Column('foto_produk', LargeBinary, nullable=False)
    launching = Column('launching', Boolean)
    deskripsi = Column('deskripsi', String(1000), nullable=False)

    material_produk = relationship('MaterialProduk', backref='produk', cascade='save-update')
    feed_back_produk = relationship('FeedBackProduk', backref='kode_produk', cascade='all')


class MaterialProduk(Base):
    __tablename__ = 'material_produk'

    kode_produk = Column('kode_produk', ForeignKey('produk.kode_produk'), primary_key=True)
    kode_material = Column('kode_material', ForeignKey('material.kode_material'), String(100), primary_key=True)
    quantitas = Column('quantitas', Integer, nullable=True)


class Material(Base):
    __tablename__ = 'material'

    kode_material = Column('kode_material', String(100), primary_key=True)
    nama_material = Column('nama_material', String(100), nullable=True)
    satuan = Column('stauan', Integer)

    material = relationship('Material', backref='material', cascade='save-update')


association_table = Table('KaryawanHandlePesanan', Base.metadata,
                          Column('kode_pesanan', ForeignKey('pesanan.kode_pesanan')),
                          Column('karyawan', ForeignKey('karyawan.nik_karyawan'))
                          )


# class KaryawanHandlePesanan(Base):
#     __tablename__ = 'karyawan_handle_pesanan'
#
#     kode_pesanan = Column(ForeignKey=True, primary_key=True)
#     nik_karyawan = Column('nik_karyawan', String(100), primary_key=True)


class Karyawan(Base):
    __tablename__ = 'karyawan'

    nik_karyawan = Column('nik_karyawan', String(100), primary_key=True)
    nama = Column('nama', String(100), nullable=False)
    alamat = Column('alamat', String(100), nullable=False)
    # password = Column('?')

    karyawan_handle_pesanan = relationship('KaryawanHandlePesanan', backref='karyawan')


class FeedBackProduk(Base):
    __tablename__ = 'feed_back_produk'

    kode_feedback = Column('kode_feedback', String(100), primary_key=True)
    kode_produk = Column('kode_produk', String(100), ForeignKey('Produk.kode_produk'))
    penilaian = Column('penilaian', String(100), ForeignKey('Produk.penilaian'))
