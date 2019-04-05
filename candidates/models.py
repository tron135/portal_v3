from django.db import models
from datetime import datetime

# Create your models here.
class Telecaller(models.Model):
    name = models.CharField(max_length=128)
    qualification = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    colname = models.CharField(max_length=256,blank=True)
    address = models.CharField(max_length=256)
    course = models.CharField(max_length=50)
    remark = models.CharField(max_length=512)
    reason = models.CharField(max_length=512)
    generated_by = models.CharField(max_length=64)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

class Enquiry(models.Model):
    telecaller_data = models.ForeignKey(Telecaller, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    dob = models.DateTimeField()
    ssc_name = models.CharField(max_length=256)
    ssc_yr = models.IntegerField()
    hsc_name = models.CharField(max_length=256)
    hsc_yr = models.IntegerField()
    dip_name = models.CharField(max_length=256)
    dip_yr = models.IntegerField()
    grad_name = models.CharField(max_length=256)
    grad_yr = models.IntegerField()
    specialization = models.CharField(max_length=128)
    status = models.CharField(max_length=64)
    source = models.CharField(max_length=64)
    file_to = models.FileField(upload_to='documents/')
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.telecaller_data

class Admission(models.Model):
    enquiry_data = models.ForeignKey(Enquiry, on_delete=models.CASCADE)
    roll_no = models.IntegerField()
    batch_code = models.CharField(max_length=128)
    batch_st_date = models.DateTimeField()
    course_code = models.CharField(max_length=64)
    add = models.CharField(max_length=256)
    area = models.CharField(max_length=64)
    pincode = models.IntegerField()
    father = models.IntegerField()
    lang = models.CharField(max_length=512)
    ssc_board = models.CharField(max_length=128)
    ssc_aggr = models.IntegerField()
    hsc_board = models.CharField(max_length=128)
    hsc_aggr = models.IntegerField()
    deg_board = models.CharField(max_length=128)
    deg_aggr = models.IntegerField()
    fst_marks = models.IntegerField()
    fst_out_of = models.IntegerField()
    fst_pass = models.IntegerField()
    fst_aggr = models.IntegerField()
    scd_marks = models.IntegerField()
    scd_out_of = models.IntegerField()
    scd_pass = models.IntegerField()
    scd_aggr = models.IntegerField()
    trd_marks = models.IntegerField()
    trd_out_of = models.IntegerField()
    trd_pass = models.IntegerField()
    trd_aggr = models.IntegerField()
    frt_marks = models.IntegerField(blank=True)
    frt_out_of = models.IntegerField(blank=True)
    frt_pass = models.IntegerField(blank=True)
    frt_aggr = models.IntegerField(blank=True)
    mdeg_board = models.CharField(max_length=128)
    mdeg_aggr = models.IntegerField(blank=True)
    mfst_marks = models.IntegerField(blank=True)
    mfst_out_of = models.IntegerField(blank=True)
    mfst_pass = models.IntegerField(blank=True)
    mfst_aggr = models.IntegerField(blank=True)
    mscd_marks = models.IntegerField(blank=True)
    mscd_out_of = models.IntegerField(blank=True)
    mscd_pass = models.IntegerField(blank=True)
    mscd_aggr = models.IntegerField(blank=True)
    exp_yr = models.IntegerField(blank=True)
    exp_mon = models.IntegerField(blank=True)
    comp_name = models.CharField(max_length=128, blank=True)
    des = models.CharField(max_length=128, blank=True)
    job_nature = models.CharField(max_length=128, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.roll_no
