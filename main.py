from fastapi import FastAPI, UploadFile, File
from different_registers import find_in_different_registers
from int_to_roman import printRoman
from read_file import get_avg_age


app = FastAPI()


@app.post("/average_age_by_position")
def upload_handler(file: UploadFile = File(...)):
    try:
        with open(file.filename, 'wb') as f:
            while contents := file.file.read(1024 * 1024):
                f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    out = get_avg_age(file.filename)
    return {"message": out}


@app.post("/find_in_different_registers")
def find_in_different_handler(words: list[str]):
    return find_in_different_registers(words)


@app.post("/int_to_roman")
def int_to_roman_handler(number: int):
    return printRoman(number)