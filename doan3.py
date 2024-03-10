import pandas as pd
import tkinter as tk
from tkinter import messagebox, simpledialog

# Đọc tệp Excel
file_mau = pd.read_excel(r'C:\Users\ADMIN\Documents\doancuoicung\esp8266.xlsx')

def calculate_average_temperature_and_humidity():
    # Lấy lựa chọn từ người dùng (ngày, tháng hoặc năm)
    choice = var.get()

    if choice == 1:  # Tính toán cho một ngày cụ thể
        # Lấy ngày từ trường nhập
        date = entry_date.get()

        # Kiểm tra xem có dữ liệu cho ngày đó không
        data_selected_date = file_mau[pd.to_datetime(file_mau['Date']).dt.date == pd.to_datetime(date).date()]
        if data_selected_date.empty:
            messagebox.showinfo("Thông báo", f"Không có dữ liệu cho ngày {date}")
            return

        # Tính nhiệt độ và độ ẩm trung bình cho ngày được chọn
        average_temperature = data_selected_date['Temp'].mean()
        average_humidity = data_selected_date['Humidity'].mean()

        # Hiển thị thông tin nhiệt độ và độ ẩm trung bình cho ngày được chọn
        label_result.config(text=f"Nhiệt độ trung bình: {average_temperature:.2f} °C\nĐộ ẩm trung bình: {average_humidity:.2f} %", fg="blue")

    elif choice == 2:  # Tính toán cho cả một tháng
        # Lấy tháng từ người dùng
        month = simpledialog.askstring("Nhập tháng", "Nhập tháng (yyyy-mm):")
        if month:
            # Kiểm tra xem có dữ liệu cho tháng đó không
            data_selected_month = file_mau[pd.to_datetime(file_mau['Date']).dt.to_period('M') == pd.to_datetime(month).to_period('M')]
            if data_selected_month.empty:
                messagebox.showinfo("Thông báo", f"Không có dữ liệu cho tháng {month}")
                return

            # Tính tổng trung bình nhiệt độ và độ ẩm cho cả tháng
            average_temperature_month = data_selected_month['Temp'].mean()
            average_humidity_month = data_selected_month['Humidity'].mean()

            # Hiển thị thông tin tổng trung bình nhiệt độ và độ ẩm cho cả tháng
            label_result.config(text=f"Nhiệt độ trung bình trong tháng: {average_temperature_month:.2f} °C\nĐộ ẩm trung bình trong tháng: {average_humidity_month:.2f} %", fg="blue")

    elif choice == 3:  # Tính toán cho cả một năm
        # Lọc dữ liệu cho cả năm 2024
        data_year_2024 = file_mau[pd.to_datetime(file_mau['Date']).dt.year == 2024]

        if data_year_2024.empty:
            messagebox.showinfo("Thông báo", "Không có dữ liệu cho năm 2024")
            return

        # Tính trung bình nhiệt độ và độ ẩm cho cả năm 2024
        average_temperature_year = data_year_2024['Temp'].mean()
        average_humidity_year = data_year_2024['Humidity'].mean()

        # Hiển thị thông tin tổng trung bình nhiệt độ và độ ẩm cho cả năm 2024
        label_result.config(text=f"Nhiệt độ trung bình trong năm 2024: {average_temperature_year:.2f} °C\nĐộ ẩm trung bình trong năm 2024: {average_humidity_year:.2f} %", fg="blue")

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Nhiệt độ và độ ẩm trung bình")
root.geometry("400x300")
root.configure(bg="lightgray")  # Đặt màu nền cho cửa sổ

# Tạo biến kiểu IntVar để lưu trữ lựa chọn của người dùng
var = tk.IntVar()

# Tạo radio button để cho phép người dùng chọn tính toán cho một ngày, một tháng hoặc cả một năm
radio_day = tk.Radiobutton(root, text="Tính toán cho một ngày", variable=var, value=1, bg="lightgray")
radio_day.pack()

radio_month = tk.Radiobutton(root, text="Tính toán cho cả một tháng", variable=var, value=2, bg="lightgray")
radio_month.pack()

radio_year = tk.Radiobutton(root, text="Tính toán cho cả một năm", variable=var, value=3, bg="lightgray")
radio_year.pack()

# Label để hiển thị hướng dẫn nhập ngày hoặc tháng
label_date = tk.Label(root, text="Nhập ngày hoặc tháng (yyyy-mm-dd hoặc yyyy-mm):", bg="lightgray")
label_date.pack()

# Trường nhập để nhập ngày hoặc tháng
entry_date = tk.Entry(root)
entry_date.pack()

# Tạo nút để tính toán và hiển thị
button_calculate = tk.Button(root, text="Tính toán", command=calculate_average_temperature_and_humidity)
button_calculate.pack()

# Label để hiển thị kết quả
label_result = tk.Label(root, text="", bg="lightgray")
label_result.pack()

root.mainloop()
