# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Acgroup(models.Model):
    groupid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    timezone1 = models.IntegerField(blank=True, null=True)
    timezone2 = models.IntegerField(blank=True, null=True)
    timezone3 = models.IntegerField(blank=True, null=True)
    holidayvaild = models.NullBooleanField()
    verifystyle = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acgroup'


class Acholiday(models.Model):
    primaryid = models.AutoField(primary_key=True)
    holidayid = models.IntegerField(blank=True, null=True)
    begindate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    timezone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acholiday'


class Actimezones(models.Model):
    timezoneid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    sunstart = models.DateTimeField(blank=True, null=True)
    sunend = models.DateTimeField(blank=True, null=True)
    monstart = models.DateTimeField(blank=True, null=True)
    monend = models.DateTimeField(blank=True, null=True)
    tuesstart = models.DateTimeField(blank=True, null=True)
    tuesend = models.DateTimeField(blank=True, null=True)
    wedstart = models.DateTimeField(blank=True, null=True)
    wedend = models.DateTimeField(blank=True, null=True)
    thursstart = models.DateTimeField(blank=True, null=True)
    thursend = models.DateTimeField(blank=True, null=True)
    fristart = models.DateTimeField(blank=True, null=True)
    friend = models.DateTimeField(blank=True, null=True)
    satstart = models.DateTimeField(blank=True, null=True)
    satend = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actimezones'


class Acunlockcomb(models.Model):
    unlockcombid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    group01 = models.IntegerField(blank=True, null=True)
    group02 = models.IntegerField(blank=True, null=True)
    group03 = models.IntegerField(blank=True, null=True)
    group04 = models.IntegerField(blank=True, null=True)
    group05 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acunlockcomb'


class Alarmlog(models.Model):
    operator = models.CharField(max_length=20, blank=True, null=True)
    enrollnumber = models.CharField(max_length=30, blank=True, null=True)
    logtime = models.DateTimeField(blank=True, null=True)
    machinealias = models.CharField(max_length=20, blank=True, null=True)
    alarmtype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alarmlog'


class Attparam(models.Model):
    paraname = models.CharField(primary_key=True, max_length=20)
    paratype = models.CharField(max_length=2, blank=True, null=True)
    paravalue = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'attparam'


class Auditedexc(models.Model):
    aeid = models.AutoField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    checktime = models.DateTimeField()
    newexcid = models.IntegerField(blank=True, null=True)
    isleave = models.IntegerField(blank=True, null=True)
    uname = models.CharField(max_length=20, blank=True, null=True)
    utime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auditedexc'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Checkexact(models.Model):
    exactid = models.AutoField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    checktime = models.DateTimeField(blank=True, null=True)
    checktype = models.CharField(max_length=2, blank=True, null=True)
    isadd = models.IntegerField(blank=True, null=True)
    yuyin = models.CharField(max_length=25, blank=True, null=True)
    ismodify = models.IntegerField(blank=True, null=True)
    isdelete = models.IntegerField(blank=True, null=True)
    incount = models.IntegerField(blank=True, null=True)
    iscount = models.IntegerField(blank=True, null=True)
    modifyby = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkexact'


class Checkinout(models.Model):
    userid = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='userid')
    checktime = models.DateTimeField()
    checktype = models.CharField(max_length=1, blank=True, null=True)
    verifycode = models.IntegerField(blank=True, null=True)
    sensorid = models.CharField(max_length=5, blank=True, null=True)
    workcode = models.IntegerField(blank=True, null=True)
    sn = models.CharField(max_length=20, blank=True, null=True)
    userextfmt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkinout'


class Departments(models.Model):
    deptid = models.AutoField(primary_key=True)
    deptname = models.CharField(max_length=30, blank=True, null=True)
    supdeptid = models.IntegerField()
    inheritparentsch = models.IntegerField(blank=True, null=True)
    inheritdeptsch = models.IntegerField(blank=True, null=True)
    inheritdeptschclass = models.IntegerField(blank=True, null=True)
    autoschplan = models.IntegerField(blank=True, null=True)
    inlate = models.IntegerField(blank=True, null=True)
    outearly = models.IntegerField(blank=True, null=True)
    inheritdeptrule = models.IntegerField(blank=True, null=True)
    minautoschinterval = models.IntegerField(blank=True, null=True)
    registerot = models.IntegerField(blank=True, null=True)
    defaultschid = models.IntegerField(blank=True, null=True)
    att = models.IntegerField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    overtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Deptusedschs(models.Model):
    deptid = models.IntegerField()
    schid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'deptusedschs'
        unique_together = (('deptid', 'schid'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Emoplog(models.Model):
    id = models.AutoField()
    userid = models.IntegerField()
    operatetime = models.DateTimeField()
    manipulationid = models.IntegerField(blank=True, null=True)
    params1 = models.IntegerField(blank=True, null=True)
    params2 = models.IntegerField(blank=True, null=True)
    params3 = models.IntegerField(blank=True, null=True)
    params4 = models.IntegerField(blank=True, null=True)
    sensorid = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emoplog'


class Excnotes(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    attdate = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'excnotes'
        unique_together = (('userid', 'attdate'),)


class Facetemp(models.Model):
    templateid = models.AutoField(primary_key=True)
    userno = models.CharField(max_length=24, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    pin = models.IntegerField(blank=True, null=True)
    faceid = models.IntegerField(blank=True, null=True)
    valid = models.IntegerField(blank=True, null=True)
    reserve = models.IntegerField(blank=True, null=True)
    activetime = models.IntegerField(blank=True, null=True)
    vfcount = models.IntegerField(blank=True, null=True)
    template = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facetemp'


class Holidays(models.Model):
    holidayid = models.AutoField(primary_key=True)
    holidayname = models.CharField(unique=True, max_length=20, blank=True, null=True)
    holidayyear = models.IntegerField(blank=True, null=True)
    holidaymonth = models.IntegerField(blank=True, null=True)
    holidayday = models.IntegerField(blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    holidaytype = models.IntegerField(blank=True, null=True)
    xinbie = models.CharField(max_length=4, blank=True, null=True)
    minzu = models.CharField(max_length=50, blank=True, null=True)
    deptid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'holidays'


class Leaveclass(models.Model):
    leaveid = models.AutoField(primary_key=True)
    leavename = models.CharField(max_length=20)
    minunit = models.FloatField()
    unit = models.IntegerField()
    remaindproc = models.IntegerField()
    remaindcount = models.IntegerField()
    reportsymbol = models.CharField(max_length=4)
    deduct = models.FloatField()
    color = models.IntegerField()
    classify = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'leaveclass'


class Leaveclass1(models.Model):
    leaveid = models.AutoField(primary_key=True)
    leavename = models.CharField(max_length=20)
    minunit = models.FloatField()
    unit = models.IntegerField()
    remaindproc = models.IntegerField()
    remaindcount = models.IntegerField()
    reportsymbol = models.CharField(max_length=4, blank=True, null=True)
    deduct = models.FloatField()
    leavetype = models.IntegerField()
    color = models.IntegerField()
    classify = models.IntegerField()
    calc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leaveclass1'


class Machines(models.Model):
    machinealias = models.CharField(max_length=20)
    connecttype = models.IntegerField()
    ip = models.CharField(max_length=20, blank=True, null=True)
    serialport = models.IntegerField(blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    baudrate = models.IntegerField(blank=True, null=True)
    machinenumber = models.IntegerField()
    ishost = models.NullBooleanField()
    enabled = models.NullBooleanField()
    commpassword = models.CharField(max_length=12, blank=True, null=True)
    uilanguage = models.IntegerField(blank=True, null=True)
    dateformat = models.IntegerField(blank=True, null=True)
    inoutrecordwarn = models.IntegerField(blank=True, null=True)
    idle = models.IntegerField(blank=True, null=True)
    voice = models.IntegerField(blank=True, null=True)
    managercount = models.IntegerField(blank=True, null=True)
    usercount = models.IntegerField(blank=True, null=True)
    fingercount = models.IntegerField(blank=True, null=True)
    secretcount = models.IntegerField(blank=True, null=True)
    firmwareversion = models.CharField(max_length=20, blank=True, null=True)
    producttype = models.CharField(max_length=20, blank=True, null=True)
    lockcontrol = models.IntegerField(blank=True, null=True)
    purpose = models.IntegerField(blank=True, null=True)
    producekind = models.IntegerField(blank=True, null=True)
    sn = models.CharField(max_length=20, blank=True, null=True)
    photostamp = models.CharField(max_length=20, blank=True, null=True)
    isifchangeconfigserver2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machines'


class NumRun(models.Model):
    num_runid = models.AutoField(primary_key=True)
    oldid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    cyle = models.IntegerField(blank=True, null=True)
    units = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'num_run'


class NumRunDeil(models.Model):
    num_runid = models.IntegerField()
    starttime = models.DateTimeField()
    endtime = models.DateTimeField(blank=True, null=True)
    sdays = models.IntegerField()
    edays = models.IntegerField(blank=True, null=True)
    schclassid = models.IntegerField(blank=True, null=True)
    overtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'num_run_deil'
        unique_together = (('num_runid', 'sdays', 'starttime'),)


class Reportitem(models.Model):
    riid = models.AutoField(primary_key=True)
    riindex = models.IntegerField(blank=True, null=True)
    showit = models.IntegerField(blank=True, null=True)
    riname = models.CharField(max_length=12, blank=True, null=True)
    unitname = models.CharField(max_length=6, blank=True, null=True)
    formula = models.TextField()
    calcbyschclass = models.IntegerField(blank=True, null=True)
    statisticmethod = models.IntegerField(blank=True, null=True)
    calclast = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reportitem'


class Schclass(models.Model):
    schclassid = models.AutoField(primary_key=True)
    schname = models.CharField(max_length=20)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    lateminutes = models.IntegerField(blank=True, null=True)
    earlyminutes = models.IntegerField(blank=True, null=True)
    checkin = models.IntegerField(blank=True, null=True)
    checkout = models.IntegerField(blank=True, null=True)
    checkintime1 = models.DateTimeField(blank=True, null=True)
    checkintime2 = models.DateTimeField(blank=True, null=True)
    checkouttime1 = models.DateTimeField(blank=True, null=True)
    checkouttime2 = models.DateTimeField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    autobind = models.IntegerField(blank=True, null=True)
    workday = models.FloatField(blank=True, null=True)
    sensorid = models.CharField(max_length=5, blank=True, null=True)
    workmins = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schclass'


class Securitydetails(models.Model):
    securitydetailid = models.AutoField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    deptid = models.IntegerField(blank=True, null=True)
    schedule = models.IntegerField(blank=True, null=True)
    userinfo = models.IntegerField(blank=True, null=True)
    enrollfingers = models.IntegerField(blank=True, null=True)
    reportview = models.IntegerField(blank=True, null=True)
    report = models.CharField(max_length=10, blank=True, null=True)
    readonly = models.NullBooleanField()
    fullcontrol = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'securitydetails'


class Serverlog(models.Model):
    id = models.AutoField()
    event = models.CharField(max_length=30)
    userid = models.IntegerField()
    enrollnumber = models.CharField(max_length=30, blank=True, null=True)
    parameter = models.IntegerField(blank=True, null=True)
    eventtime = models.DateTimeField()
    sensorid = models.CharField(max_length=5, blank=True, null=True)
    operator = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serverlog'


class Shift(models.Model):
    shiftid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    ushiftid = models.IntegerField(blank=True, null=True)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField(blank=True, null=True)
    runnum = models.IntegerField(blank=True, null=True)
    sch1 = models.IntegerField(blank=True, null=True)
    sch2 = models.IntegerField(blank=True, null=True)
    sch3 = models.IntegerField(blank=True, null=True)
    sch4 = models.IntegerField(blank=True, null=True)
    sch5 = models.IntegerField(blank=True, null=True)
    sch6 = models.IntegerField(blank=True, null=True)
    sch7 = models.IntegerField(blank=True, null=True)
    sch8 = models.IntegerField(blank=True, null=True)
    sch9 = models.IntegerField(blank=True, null=True)
    sch10 = models.IntegerField(blank=True, null=True)
    sch11 = models.IntegerField(blank=True, null=True)
    sch12 = models.IntegerField(blank=True, null=True)
    cycle = models.IntegerField(blank=True, null=True)
    units = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shift'


class Systemlog(models.Model):
    operator = models.CharField(max_length=20, blank=True, null=True)
    logtime = models.DateTimeField(blank=True, null=True)
    machinealias = models.CharField(max_length=20, blank=True, null=True)
    logtag = models.IntegerField(blank=True, null=True)
    logdescr = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'systemlog'


class Tbkey(models.Model):
    prename = models.CharField(max_length=12, blank=True, null=True)
    onekey = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbkey'


class Tbsmsallot(models.Model):
    reference = models.IntegerField(primary_key=True)
    smsref = models.IntegerField()
    userref = models.IntegerField()
    gentm = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbsmsallot'


class Tbsmsinfo(models.Model):
    reference = models.IntegerField(primary_key=True)
    smsid = models.CharField(max_length=16)
    smsindex = models.IntegerField()
    smstype = models.IntegerField(blank=True, null=True)
    smscontent = models.TextField(blank=True, null=True)
    smsstarttm = models.CharField(max_length=20, blank=True, null=True)
    smstmleng = models.IntegerField(blank=True, null=True)
    gentm = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbsmsinfo'


class Template(models.Model):
    templateid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    fingerid = models.IntegerField()
    template = models.TextField()
    template2 = models.TextField(blank=True, null=True)
    bitmappicture = models.TextField(blank=True, null=True)
    bitmappicture2 = models.TextField(blank=True, null=True)
    bitmappicture3 = models.TextField(blank=True, null=True)
    bitmappicture4 = models.TextField(blank=True, null=True)
    usetype = models.IntegerField(blank=True, null=True)
    template3 = models.TextField(blank=True, null=True)
    emachinenum = models.CharField(max_length=3, blank=True, null=True)
    template1 = models.TextField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    divisionfp = models.IntegerField(blank=True, null=True)
    template4 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template'
        unique_together = (('userid', 'fingerid'),)


class UserOfRun(models.Model):
    userid = models.IntegerField()
    num_of_run_id = models.IntegerField()
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    isnotof_run = models.IntegerField(blank=True, null=True)
    order_run = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_of_run'
        unique_together = (('userid', 'num_of_run_id', 'startdate', 'enddate'),)


class UserSpeday(models.Model):
    userid = models.IntegerField()
    startspecday = models.DateTimeField()
    endspecday = models.DateTimeField(blank=True, null=True)
    dateid = models.IntegerField()
    yuanying = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_speday'
        unique_together = (('userid', 'startspecday', 'dateid'),)


class UserTempSch(models.Model):
    userid = models.IntegerField()
    cometime = models.DateTimeField()
    leavetime = models.DateTimeField()
    overtime = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    schclassid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_temp_sch'
        unique_together = (('userid', 'cometime', 'leavetime'),)


class Useracmachines(models.Model):
    userid = models.IntegerField()
    deviceid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'useracmachines'
        unique_together = (('userid', 'deviceid'),)


class Useracprivilege(models.Model):
    userid = models.IntegerField(primary_key=True)
    acgroupid = models.IntegerField()
    isusegroup = models.NullBooleanField()
    timezone1 = models.IntegerField(blank=True, null=True)
    timezone2 = models.IntegerField(blank=True, null=True)
    timezone3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'useracprivilege'


class Userinfo(models.Model):
    userid = models.AutoField(primary_key=True)
    badgenumber = models.CharField(unique=True, max_length=24)
    ssn = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=8, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    pager = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    hiredday = models.DateTimeField(blank=True, null=True)
    street = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=2, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=12, blank=True, null=True)
    ophone = models.CharField(max_length=20, blank=True, null=True)
    fphone = models.CharField(max_length=20, blank=True, null=True)
    verificationmethod = models.IntegerField(blank=True, null=True)
    defaultdeptid = models.ForeignKey(Departments, models.DO_NOTHING, db_column='defaultdeptid', blank=True, null=True)
    securityflags = models.IntegerField(blank=True, null=True)
    att = models.IntegerField()
    inlate = models.IntegerField()
    outearly = models.IntegerField()
    overtime = models.IntegerField()
    sep = models.IntegerField()
    holiday = models.IntegerField()
    minzu = models.CharField(max_length=8, blank=True, null=True)
    lunchduration = models.IntegerField()
    mverifypass = models.CharField(max_length=10, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    inheritdeptsch = models.IntegerField(blank=True, null=True)
    inheritdeptschclass = models.IntegerField(blank=True, null=True)
    autoschplan = models.IntegerField(blank=True, null=True)
    minautoschinterval = models.IntegerField(blank=True, null=True)
    registerot = models.IntegerField(blank=True, null=True)
    inheritdeptrule = models.IntegerField(blank=True, null=True)
    emprivilege = models.IntegerField(blank=True, null=True)
    cardno = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    privilege = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'


class Usersmachines(models.Model):
    id = models.AutoField()
    userid = models.IntegerField()
    deviceid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usersmachines'


class Userupdates(models.Model):
    updateid = models.AutoField(primary_key=True)
    badgenumber = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userupdates'


class Userusedsclasses(models.Model):
    userid = models.IntegerField()
    schid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userusedsclasses'
        unique_together = (('userid', 'schid'),)
