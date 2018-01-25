# BMI值計算公式:    BMI = 體重(公斤) / 身高^(公尺^)

weight = input('請輸入體重(公斤): ')
height = input('請輸入身高(公尺): ')

bmi = float(weight) / float(height) / float(height)
if bmi < 18.5:
	print('體重過輕')
elif bmi < 24 and bmi >= 18.5:
	print('正常範圍')
elif bmi >= 24 and bmi < 27:
	print('稍重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
else:
	print('重度肥胖')
