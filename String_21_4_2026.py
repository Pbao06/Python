
import re
def Chuan_Hoa_Chuoi(s):
    s=s.strip() 
    s=re.sub(r'\s+','',s)
    s = re.sub(r'\s+([.,])', r'\1', s)
    return s

s=input(" Nhap vao chuoi:")
output_str = Chuan_Hoa_Chuoi(s)
print(f"Gốc: '{s}'")
print(f"Sau khi chuẩn hóa: '{output_str}'")
