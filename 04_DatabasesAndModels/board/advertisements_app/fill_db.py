from .models import Advertisement
import datetime


def fill_db(number):
    for i in range(0, number):
        new_advertisement = Advertisement(title='Объявление ' + str(i),
                                          description='Текст объявления' + str(i),
                                          price=i,
                                          created_at=datetime.datetime.now(),
                                          update_at=datetime.datetime.now(),
                                          views_count=i

                                          )
        new_advertisement.save()


