from django.db import models

# Create your models here.

class Convocatoria(models.Model):
    NroConv = models.IntegerField(null=False, primary_key=True)
    CodCli = models.IntegerField()
    FecPubli = models.DateField()
    FecBuenaPro = models.DateField()
    Nomenclatura = models.CharField(max_length=100)
    FecReinicio = models.DateField()
    CodObjC = models.IntegerField()
    DescObjeto = models.CharField(max_length=1000)
    CodSNIP = models.CharField(max_length=10)
    ValRefer = models.DecimalField(max_digits=9, decimal_places=2)
    RutaDoc = models.CharField(max_length=300)

#    def __str__(self):
#        return self.NroConv
    def __str__(self):
        return 'Convocatoria: {} {} {} {} {} {} {} {} {} {} {} '.format(self.NroConv, self.CodCli, self.FecPubli, self.FecBuenaPro, self.Nomenclatura, self.FecReinicio, self.CodObjC, self.DescObjeto, self.CodSNIP, self.ValRefer, self.RutaDoc)

class ResulConv(models.Model):
    NroConv = models.ForeignKey('Convocatoria', db_column='NroConv', on_delete=models.CASCADE)
    CorrConv = models.IntegerField(primary_key=True)
    Empresa = models.CharField(max_length=200)
    FlgGana = models.CharField(max_length=1)
    EvalTec = models.DecimalField(max_digits=5, decimal_places=2)
    EvalEcon = models.DecimalField(max_digits=5, decimal_places=2)
    Observac = models.CharField(max_length=2000)

#    def __str__(self):
#        return self.CorrConv
    def __str__(self):
        return 'Resultado Convocatoria: {} {} {} {} {} {} '.format(self.CorrConv, self.Empresa, self.FlgGana, self.EvalTec, self.EvalEcon, self.Observac)


class ConvPers(models.Model):
    NroConv = models.ForeignKey('Convocatoria', db_column='NroConv', on_delete=models.CASCADE)
    CodPers = models.IntegerField()
    CodCargo = models.IntegerField()
    Experiencia = models.CharField(max_length=500)
    ExpNroMeses = models.IntegerField()
    ExpNroDias = models.IntegerField()
    CorrProf = models.IntegerField()
    FlgCIPVigen = models.IntegerField()

    def __str__(self):
        return 'Resultado Convocatoria: {} {} {} {} {} {} {} '.format(self.CodPers, self.CodCargo, self.Experiencia, self.ExpNroMeses, self.ExpNroDias, self.CorrProf, self.FlgCIPVigen)
