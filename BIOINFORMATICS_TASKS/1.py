# _*_ coding: utf-8

import subprocess
import os.path
from pathlib import Path
import argparse
import getpass
import sys
import re
import gc
import openpyxl
import pandas
from openpyxl import load_workbook


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--one', help="The first file to alignment",
                        default="/media/drsnail/Linux/Test_Genome/wgEncodeHaibRnaSeqT47dEstradia4hRawDataRep1.fastq")
    parser.add_argument('--two', help="The second file to alignment")
    parser.add_argument('--Uniq', help="The unpaired file to alignment")
    parser.add_argument("-b", "--bamfile", help=".bamfile is required",
                        default="/media/drsnail/Linux/Test_Genome/new.bam")
    parser.add_argument('-f', '--reference',
                        help="reference file is required. The path should start from '/'. For example: -f /media/drsnail/Linux/Test Genome/genome_snp.fa",
                        default=r"C:\Users\guard\Downloads\chrY.fa")
    parser.add_argument('-t', '--templocation', help="Due processing some temp file will have been created",
                        default="/media/drsnail/Linux/Test_Genome/")
    parser.add_argument('-e', '--excel', help="Sepcify for working with excel file")
    parser.add_argument('-i', help="bcftools view [-i argument]")
    return parser

class RefMassive():
    def __init__(self, referencefile_adress):
        self.referencefile_adress = referencefile_adress
        self.reference_shortname = re.search(r"\w+\.fa", self.referencefile_adress)[0]
        self.reference_shortname = re.split(r"\.", self.reference_shortname)[0]
        # self.reference_shortname = os.path.join(re.search(r"/.+/", self.referencefile_adress)[0],
        #                                         self.reference_shortname)
        self.two_dimensional_list = False
        self.__get_massive()

    # Функция прочитывает все строки из референсного файла
    def __get_massive(self):
        with open("{reference}".format(reference=self.referencefile_adress), "r") as f:
            self.reference_massive = f.readlines()
            self.lenght = len(self.reference_massive[1]) - 1

    def count_ATGC(self):
        """
        Функция только для одномерного массива. Считает количество ATGC + позиции N
        :return: None
        :rtype:
        """
        if self.two_dimensional_list == False:
            self.A = 0
            self.T = 0
            self.G = 0
            self.C = 0
            self.N = []
            i = 0
            temp_massive = self.reference_massive[1:]
            temp_massive.reverse()
            for line in temp_massive:
                for pos in line:
                    i += 1
                    if pos == ("A" or "a"):
                        self.A += 1
                    elif pos == ("T" or "t"):
                        self.T += 1
                    elif pos == ("G" or "g"):
                        self.G += 1
                    elif pos == ("C" or "c"):
                        self.C += 1
                    else:
                        self.N.append([i])
        else:
            raise NameError

    # Находит индексы, где массив содержит название хромосомы, затем возвращает в это же место только лишь название хромосомы
    def sort_reference_by_chr(self, short=False):
        """
    Находит индексы, где массив содержит название хромосомы, затем возвращает в это же место только лишь название хромосомы
        :param short: - True если в референсном файле хромосомы указываются в формате >1 >2 >3 и т.д.
        :type short: Boolean
        :return: None
        :rtype: None
        """
        pos = []
        for indx in range(0, len(self.reference_massive)):
            match = re.search("(\>)(\w+)", self.reference_massive[indx])
            if match != None:
                pos.append(indx)
                if short == False:
                    self.reference_massive[indx] = match[0] + "\n"
                else:
                    self.reference_massive[indx] = ">chr" + match[2] + "\n"
        return pos

    # Далет двумерный массив, разрезая массив от позиции и до позиции. В качестве pos передавался массив с позициями названий хромосом
    def sub_massive(self, pos):
        """
        Далет двумерный массив, разрезая массив от позиции и до позиции. В качестве pos передавался массив с позициями названий хромосом
        :param pos: Передается массив содержащий индексы хромосомы
        :return: ничего
        """
        q = pos
        new_massive = []
        for q_len in range(0, len(q)):
            try:
                from_ = q[q_len]
                to_ = q[q_len + 1]
                new_massive.append(self.reference_massive[from_:to_])
            except IndexError:
                from_ = q[q_len]
                new_massive.append(self.reference_massive[from_:])
        self.reference_massive = new_massive
        self.two_dimensional_list = True

    # Получить строку референсного файла из нужной позиции
    def get_line(self, pos):
        tpos = int(pos) - 1
        line = tpos // self.lenght + 1  # целая часть от деления + 1, так как первый элемент массива - название хромосомы
        return line

    # Получить позицию в строке референсного файла
    def get_subpos(self, pos):
        tpos = int(pos) - 1
        subpos = tpos % self.lenght  # self.lenght = 50
        return subpos

    # Комплексный метод вызывающий get_line & get_ subpos
    def get_position(self, pos):
        line = self.get_line(pos)
        subpos = self.get_subpos(pos)
        return line, subpos

    # Делает замены в референсном файле, в нужной позиции на нужную букву
    def substitution_in_postition(self, pos, substitution):
        line, subpos = self.get_position(pos)
        # print(self.tref_massive[line])
        temp_massive = self.reference_massive[line]
        self.reference_massive[line] = temp_massive[:subpos] + substitution + temp_massive[subpos + 1:]

    # Делает замены в референсном файле, в нужной позиции на нужную букву
    def __substition_in_postition(self, pos, substitution, tref_massive):
        line, subpos = self.get_position(pos)
        # print(tref_massive[line])
        temp_massive = tref_massive[line]
        tref_massive[line] = temp_massive[:subpos] + substitution + temp_massive[subpos + 1:]
        return tref_massive

    # Замена в определенной хромосоме
    def substitution_chr(self, chr, pos, substitution, short):
        if self.two_dimensional_list == True:
            pass
        elif self.two_dimensional_list == False:
            self.sub_massive(self.sort_reference_by_chr(short=short))
        else:
            raise NameError
        # Поиск индекса массива по этой хромосоме
        for i in range(0, len(self.reference_massive)):
            if chr in self.reference_massive[i][0]:
                self.reference_massive[i] = self.__substition_in_postition(pos=pos, substitution=substitution,
                                                                           tref_massive=self.reference_massive[i])
                break

    # Записывает новый референсный файл
    def write_all(self, tempfiles_location, referencefile_name=''):
        if referencefile_name != '':
            alter_reference_adress = os.path.join(tempfiles_location, referencefile_name)
        else:
            alter_reference_adress = tempfiles_location
        with open(alter_reference_adress, "w") as f:
            for i in self.reference_massive:
                f.writelines(i)

    # Функция запускающая индексацию референсного файла
    def bowtie2_build(self):
        subprocess.check_call(r"bowtie2-build {name} {output_name}".format(name=self.referencefile_adress,
                                                                           output_name=self.reference_shortname),
                              shell=True)

    # Выравнивание с помощью Bowtie2
    def bowtie2_alligment(self, reference, is_paired, filename1, samname, filename2=''):
        if is_paired == True:
            subprocess.check_call(
                "bowtie2 -q -x {reference} -1 {filename1} -2 {filename2} -S {samname} --threads 6".format(
                    reference=reference, filename1=filename1, filename2=filename2, samname=samname), shell=True)
        elif is_paired == False:
            subprocess.check_call(
                "bowtie2 -q -x {reference} -U {filename1} -S {samname} --threads 6".format(reference=reference,
                                                                                           filename1=filename1,
                                                                                           samname=samname), shell=True)
        else:
            print('ERROR! Bowtie2_alligment')

    # Выравнивание с помощью hisat2
    def hisat2_alligment(self, reference, is_paired, filename1, samname, filename2=''):
        if is_paired == True:
            subprocess.check_call(
                "hisat2 -q -x {reference} -1 {filename1} -2 {filename2} -S {samname} --threads 6".format(
                    reference=reference, filename1=filename1, filename2=filename2, samname=samname), shell=True)
        elif is_paired == False:
            subprocess.check_call(
                "hisat2 -q -x {reference} -U {filename1} -S {samname} --threads 6".format(reference=reference,
                                                                                          filename1=filename1,
                                                                                          samname=samname), shell=True)
        else:
            print('ERROR! hisat2_alligment')



parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

reference = RefMassive(namespace.reference)
reference.count_ATGC()
print(reference.A)
print(len(reference.reference_massive))
index_from, pos_from = reference.get_position(100000)
index_to, pos_to = reference.get_position(100100)
temp_reference = "".join(reference.reference_massive).
temp_reference = re.sub(r"\n", temp_reference)
print(len(reference.reference_massive))