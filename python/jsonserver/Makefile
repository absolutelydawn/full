all:
	uvicorn app:app --host 0.0.0.0 --port 8000 --reload &
kill:
	kill -9 `ps -ef | grep app | cut -d " " -f8`