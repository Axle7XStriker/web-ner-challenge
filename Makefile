default:
	@echo "An explicit target is required"

install:
	cd flask-backend && pip install -r requirements.txt

start:
	cd flask-backend && flask run
