from classManager import *


def inputMenuUser():
    return input('[C]ari | '
                 '[D]aftar | '
                 '[P]esan\n'
                 '--> ').lower()


class Buyer(Manager, Ticket):
    def __init__(self, terbang, armada, rute, tiket):
        Manager.__init__(self, terbang, armada, rute, tiket)
        # Ticket.__init__(self, tiket)
        # self.tiket =
        pass

    def cariData(self):
        menu = None
        while menu != 'k':
            if menu == 'd':
                cari = input('Masukkan Kota keberangkatan\n'
                             '--> ')
                if cari in self._depart:
                    print(f'{cari} Tersedia!')
                    # Kasih info jika ingin beli Tiket rute ini
                    self.pesanTiket()
                    pass

                pass
            elif menu == 'a':
                cari = input('Masukkan kota tujuan\n'
                             '-->')
                if cari in self._arrive:
                    print(f'{cari} Tersedia!')
                pass
            menu = penerbangan()
        pass

    def pesanTiket(self):
        # Milih rute
        # -->
        # Milih Tipe Tiket (regular, premium, firstclass)
        # -->
        # Menampilkan jumlah pembayaran
        # -->
        pass

    def outputData(self):
        menu = None
        while menu != 'k':
            if menu == 'd':
                self.output(self._rute)
            elif menu == 't':
                self.tiket.outputData()
            elif menu == 'a':
                self.output(self._armada)
            menu = input()

    pass
