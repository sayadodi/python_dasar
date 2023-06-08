class Ac:
    suhu = 16
    statusAc = 'mati'

    def hidupKan(self):
        self.statusAc = 'hidup'
        print('Ac dihidupkan')

    def matikan(self):
        self.statusAc = 'mati'
        print('Ac dimatikan')

    def naikkanSuhu(self):
        self.suhu += 1
        print('Suhu Ac Dinaikkan')

    def turunkanSuhu(self):
        self.suhu -= 1
        print('Suhu Ac Diturunkan')

    def info(self):
        print('Kondis AC Saat ini', self.statusAc,
              'Dengan Suhu', self.suhu, '°C')


politron = Ac()
politron.info()
politron.hidupKan()
politron.info()
politron.naikkanSuhu()
politron.info()
politron.turunkanSuhu()
politron.info()
politron.matikan()
politron.info()
