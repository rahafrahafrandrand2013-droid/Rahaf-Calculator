import math
import cmath

def professional_calculator():
    print("--- آلة رهف الحاسبة الاحترافية (نسخة الرياضيات الكاملة) ---")
    print("المميزات: دعم الجذور، الأسس، العمليات التخيلية، والتعامل مع الأخطاء.")
    print("اكتبي 'خروج' للإنهاء.")
    
    while True:
        expression = input("\nأدخلي العملية الرياضية (مثال: 5**2 + sqrt(16)): ")
        
        if expression.lower() == 'خروج':
            print("شكراً لاستخدام آلة رهف. مع السلامة!")
            break
            
        try:
            # قاموس للتحويل الرياضي الذكي
            allowed_names = {
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "pi": math.pi,
                "e": math.e,
                "log": math.log,
                "csqrt": cmath.sqrt # للجذور السالبة
            }
            
            # تنفيذ العملية الحسابية بأمان
            # نستخدم eval مع تقييد الوصول للمتغيرات لحماية النظام
            result = eval(expression, {"__builtins__": None}, allowed_names)
            
            # عرض النتيجة بتنسيق دقيق
            if isinstance(result, complex):
                print(f"النتيجة: {result.real:.2f} + {result.imag:.2f}i")
            else:
                print(f"النتيجة: {result}")
                
        except ZeroDivisionError:
            print("خطأ رياضي: لا يمكن القسمة على صفر!")
        except Exception as e:
            print(f"خطأ: تأكدي من كتابة المعادلة بشكل صحيح. ({e})")

# تشغيل الآلة
professional_calculator()
