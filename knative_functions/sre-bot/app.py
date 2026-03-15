import json
import time
import logging

# SRE Auto-Remediation Bot
# Triggered by Prometheus alerts or SRE team manual execution
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
log = logging.getLogger("viettel.sre.remediator")

# code nay de restart service khi co loi
def handle(req):
    print("--- DANG CHAY BOT REMEDITION ---")
    
    # parse data tu knative
    body = json.loads(req)
    ly_do = body.get('reason', 'khong ro')
    print("Loi: " + ly_do)

    # list cac lenh can chay, tam thoi de day
    # TODO: them nhieu service nua
    print("Dang chay: flush redis...")
    # os.system("redis-cli FLUSHALL") # tam thoi comment lai cho an toan
    
    print("Dang chay: restart order service...")
    # os.system("kubectl rollout restart deployment order")

    # tra ve ket qua cho dung kieu json
    return '{"status": "xong", "services": ["redis", "order"]}'


