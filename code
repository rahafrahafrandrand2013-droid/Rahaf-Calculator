def generate_study_schedule():
    print("--- مرحباً بك في مخطط الدراسة الذكي ---")
    
    # طلب المدخلات من المستخدم
    total_hours = float(input("كم ساعة متاحة للدراسة اليوم؟ "))
    num_subjects = int(input("كم مادة تريد دراستها؟ "))
    
    subjects = []
    total_difficulty = 0
    
    # جمع بيانات المواد
    for i in range(num_subjects):
        name = input(f"اسم المادة {i+1}: ")
        difficulty = int(input(f"ما مدى صعوبة المادة {name} (من 1 إلى 10)؟ "))
        subjects.append({"name": name, "difficulty": difficulty})
        total_difficulty += difficulty
        
    print("\n--- جدولك الدراسي المقترح ---")
    
    # الحسابات: توزيع الساعات بناءً على الصعوبة
    for subject in subjects:
        # النسبة المئوية للصعوبة * إجمالي الساعات
        share = (subject["difficulty"] / total_difficulty) * total_hours
        print(f"المادة: {subject['name']} | وقت الدراسة المقترح: {share:.2f} ساعة")

    print("\nملاحظة: هذا الجدول تم إنتاجه بواسطة كود بايثون مخصص للتميز الدراسي.")

# تشغيل البرنامج
if __name__ == "__main__":
    generate_study_schedule()
