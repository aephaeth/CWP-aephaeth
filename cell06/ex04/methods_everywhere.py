#!/usr/bin/env python3
import sys


def shrink(s):
  # ใช้ Slice เพื่อตัดข้อความเอาแค่ 8 ตัวอักษรแรก
  print(s[:8])


def enlarge(s):
  # เติมตัว 'Z' ต่อท้ายจนกว่าจะครบ 8 ตัวอักษร
  print(s + "Z" * (8 - len(s)))


def main():
  args = sys.argv[1:]
  # ถ้าไม่มีพารามิเตอร์ส่งมาเลย
  if len(args) < 1:
    print("none")
  else:
    for arg in args:
      if len(arg) > 8:
        shrink(arg)
      elif len(arg) < 8:
        enlarge(arg)
      else:
        print(arg)


if __name__ == "__main__":
  main()