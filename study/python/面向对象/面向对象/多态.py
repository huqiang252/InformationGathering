#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-28
# 中医
# 中医
class Father:
    def cure(self):
        print("使用中医方法进行治疗。。。")

# 西医
class Son(Father):
    def cure(self):
        print("使用西医方法进行治疗。。。")

# 兽医
class AnimalDoctor:
    def cure(self):
        print("使用兽医方法进行治疗。。。")

# # 患者
# class Patient:
#     def needDoctor(self, doctor):
#         doctor.cure()


# 类型检查后的优化 （患者）
class Patient:
    def needDoctor(self, doctor):
        if issubclass(doctor.__class__, Father):
            doctor.cure()
        else:
            print("此大夫医疗方法不适用病人。。。")



if __name__ == '__main__':
    oldDoctor = Father()
    littleDoctor = Son()
    animalDoctor = AnimalDoctor()

    patient = Patient()

    patient.needDoctor(oldDoctor)
    patient.needDoctor(littleDoctor)
    patient.needDoctor(animalDoctor)



