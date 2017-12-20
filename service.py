from models import *


def form_data():
    data = get_data()
    info_data = data.get('info')
    head = data.get('key')
    head.append("web_id")
    max_id = data.get('max_id')
    new_info = {i: '' for i in head}
    new_info.update({"web_id": max_id + 1})
    return dict(info_data=info_data, head=head, new_info=new_info)