FROM python:3.11
RUN pip install Flask==3.0
RUN pip install tensorflow==2.15.0

COPY inference_server.py /inference_server.py
COPY models/hurricane_lenet5a_model.keras /model.keras
COPY configs.json /configs.json

CMD ["python3", "inference_server.py"]
# CMD ["sleep", "infinity"] (used for debugging)