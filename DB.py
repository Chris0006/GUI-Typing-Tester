import shelve

def restart_record():
    rec = shelve.open('wpm_record1-shelve')
    rec['record'] = 0
    rec.close()

restart_record()
