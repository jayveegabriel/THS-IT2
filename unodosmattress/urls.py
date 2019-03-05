from django.conf.urls import url
from unodosmattress import views
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    url(r'^clickButton/(?P<idBed>[0-9]+)/$', views.clickButton, name="clickButton"),
    url(r'^ajax/ajaxGetClicked/$', views.ajaxGetClicked, name="ajaxGetClicked"),
    url(r'^ajax/ajaxClearClicked/$', views.ajaxClearClicked, name="ajaxClearClicked"),
    url(r'^ajax/ajaxGetNewNotifications/$', views.ajaxGetNewNotifications, name="ajaxGetNewNotifications"),
    url(r'^ajax/ajaxGetNotifications/$', views.ajaxGetNotifications, name="ajaxGetNotifications"),
    url(r'^ajax/ajaxGetNewNotificationsSize/$', views.ajaxGetNewNotificationsSize, name="ajaxGetNewNotificationsSize"),
    url(r'^ajax/ajaxClearNewNotifications/$', views.ajaxClearNewNotifications, name="ajaxClearNewNotifications"),

    url(r'^ajax/ajaxGetCurrentRFIDs/$', views.ajaxGetCurrentRFIDs, name="ajaxGetCurrentRFIDs"),



    url(r'^login/$', views.login, name = "login"),
        url(r'^ajax/loginUsername/$', views.loginUsername, name = "loginUsername"), #ADDED
    url(r'^ajax/loginChecker/$', views.loginChecker, name = "loginChecker"),
    url(r'^blocked/$', views.blocked, name = "blocked"),


    #nurse
    url(r'^dashboard/$', views.dashboard, name = "dashboard"),
    url(r'^notifications/$', views.notifications, name ="notifications"),
    url(r'^managepatients/$', views.managepatients, name="managepatients"),
    # url(r'^managebeds/$', views.managebeds, name="managebeds"),
    # url(r'^reports/$', views.reports, name="reports"),
    url(r'^viewpatients/(?P<idPatient>[0-9]+)/$', views.viewpatients, name="viewpatients"),
    # path('/viewpatients/<int:idPatient/', views.viewpatients, name="viewpatients"),
        
    url(r'^ajax/displayDoctors/$', views.ajaxDisplayDoctors, name="ajaxDisplayDoctors"),
    url(r'^ajax/getAvailableBeds/$', views.ajaxGetAvailableBeds, name="ajaxGetAvailableBeds"),
    url(r'^ajax/ajaxGetPatients/$', views.ajaxGetPatients, name="ajaxGetPatients"),
    url(r'^ajax/ajaxUpdateDashboard/$', views.ajaxUpdateDashboard, name="ajaxUpdateDashboard"),
    url(r'^ajax/ajaxUpdateStatusPatient/$', views.ajaxUpdateStatusPatient, name="ajaxUpdateStatusPatient"),
    url(r'^ajax/getDoctorInfo/$', views.getDoctorInfo, name="getDoctorInfo"),

    url(r'^ajax/rfidCount/$', views.ajaxrfidCount, name="ajaxrfidCount"),

    #api
    url(r'^temperature/$', views.TemperatureList.as_view(), name='temperature-list'),
    url(r'^temperature/(?P<pk>[0-9]+)/$', views.TemperatureDetail.as_view(), name='temperature-detail'),
    url(r'^heartrate/$', views.HeartRateList.as_view(), name='heartRate-list'),
    url(r'^heartrate/(?P<pk>[0-9]+)/$', views.HeartRateDetail.as_view(), name='heartRate-detail'),

    url(r'^temperatureEveryMin/$', views.TemperatureEveryMinList.as_view(), name='temperatureEveryMin-list'),
    url(r'^temperatureEveryMin/(?P<pk>[0-9]+)/$', views.TemperatureEveryMinDetail.as_view(), name='temperatureEveryMin-detail'),
    url(r'^heartrateEveryMin/$', views.HeartRateEveryMinList.as_view(), name='heartRateEveryMin-list'),
    url(r'^heartrateEveryMin/(?P<pk>[0-9]+)/$', views.HeartRateEveryMinDetail.as_view(), name='heartRateEveryMin-detail'),

    url(r'^beds/$', views.BedList.as_view(), name='bed-list'),
    url(r'^beds/(?P<pk>[0-9]+)/$', views.BedDetail.as_view(), name='bed-detail'),
    url(r'^rfid/$', views.RFIDList.as_view(), name='rfid-list'),
    url(r'^rfid/(?P<pk>[0-9]+)/$', views.RFIDDetail.as_view(), name='rfid-detail'),
    url(r'^position/$', views.PositionList.as_view(), name='position-list'),
    url(r'^position/(?P<pk>[0-9]+)/$', views.PositionDetail.as_view(), name='position-detail'),
    # url(r'^notification/$', views.NotificationList.as_view(), name='notification-list'),
    # url(r'^notification/(?P<pk>[0-9]+)/$', views.NotificationDetail.as_view(), name='notification-detail'),



    #admin
    url(r'^$login/', views.login, name = "login"),
    url(r'^home/$', views.home, name = "home"),
    url(r'^admin/manageusers/$', views.manageusers, name="manageusers"),
    url(r'^admin/managebeds/$', views.managebeds, name="managebeds"),
    url(r'^viewusers/(?P<username>[\w\-]+)/$', views.viewusers, name="viewusers"),
    url(r'^ajax/setBedAvailable/$', views.ajaxSetBedAvailable, name="ajaxSetBedAvailable"),
    url(r'^ajax/getPendingBeds/$', views.ajaxGetPendingBeds, name="ajaxGetPendingBeds"),
    url(r'^ajax/checkUser/$', views.ajaxCheckUser, name="ajaxCheckUser"),
    url(r'^ajax/saveNewPassword/$', views.ajaxSaveNewPassword, name="ajaxSaveNewPassword"),
    url(r'^ajax/ajaxUpdateBedStatus/$', views.ajaxUpdateBedStatus, name="ajaxUpdateBedStatus"),
    url(r'^ajax/ajaxRefreshAvailableBeds/$', views.ajaxRefreshAvailableBeds, name="ajaxRefreshAvailableBeds"),
    url(r'^ajax/ajaxRefreshUnavailableBeds/$', views.ajaxRefreshUnavailableBeds, name="ajaxRefreshUnavailableBeds"),
    url(r'^ajax/updateAccountStatus/$', views.updateAccountStatus, name="updateAccountStatus"),


    #doctor

    url(r'^doctor/home/$', views.doctorhome, name="doctorhome"),
    url(r'^doctor/mypatients/$', views.mypatients, name="mypatients"),
    url(r'^doctor/reports/(?P<pk>[0-9]+)/$', views.reports, name="reports"),
    url(r'^doctor/patients/$', views.patients, name="patients"),

    url(r'^logout/$', views.logout, name="logout"),
    url(r'^ajax/ajaxGetEveryMinHeartRate/$', views.ajaxGetEveryMinHeartRate, name="ajaxGetEveryMinHeartRate"),

    url(r'^doctor/view/(?P<pk>[0-9]+)/$', views.view, name="view"),




    #newly added
    url(r'^ajax/ajaxSelectRoom/',views.ajaxSelectRoom, name="ajaxSelectRoom"),
    url(r'^ajax/ajaxConfirmationUsername/',views.ajaxConfirmationUsername, name="ajaxConfirmationUsername"),
    url(r'^ajax/ajaxGetUpdatedDashboard/',views.ajaxGetUpdatedDashboard, name="ajaxGetUpdatedDashboard"),
    url(r'^ajax/ajaxLoadData/',views.ajaxLoadData, name="ajaxLoadData"),
    url(r'^ajax/ajaxUpdateBedOptions/',views.ajaxUpdateBedOptions, name="ajaxUpdateBedOptions"),
    url(r'^ajax/ajaxGetQFifteen/',views.ajaxGetQFifteen, name="ajaxGetQFifteen"),

    url(r'^ajax/ajaxGetQOne/',views.ajaxGetQOne, name="ajaxGetQOne"),

    
]
