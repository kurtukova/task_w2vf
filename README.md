������ script.py ������������ ��� ���������� ������ � �������, �������� ������� word2vecf �� ������� ������� �� ���������� �����.
������ ��� ��������� ���������������� � ������� �������� � ������ word2vecf ������ � ��������, �������������� conll-u ������, � ����� ���:
"�����" ������ "��������"
��� ��������� ��������� � ���������� ��������������� ������ ������������ ���������� spaCy.
���������� ������ �� ����� ���������� ���������. ������ ������ ������� �� �����������. ����� ��� ������� ����� ������������ ��������.
�������� ����� ����� ���:
child/dep_head/dep-1
��� child - ������� ������� ����� � �������������� ������ (����� ���� ���������), dep - �������������� ����� ����� � ��������
head - �������� ����� � �������������� ������, dep-1 - �������������� ����� ����� � ���������
����� ������������ "�������" ���������� ��������� ���� ��� �������������� ����� prep (�������) ����� ��� � ������.

������������� �������:
script.py --in <������� ����> --out <�������� ����>
��������� �� ���������: 
--in corpus.txt
--out dep.contexts 

��� �������� ������������ ��� ��������� � �����. �� ���� �� ����� ������ ����� ������� ���� ��������� � ubuntu, ����� ������� ���������

1. ������� ����������: 
docker build -t task_w2vf . 

2. ������: 
docker run -it -v $pwd/share:/root/share task_w2vf 
� ������� ����� /share ����� ��������� ����� � ����������, �.�. �� ����� ������������� � ���������� ���������� ��� ������� ������ �����. 
���� � ����� ������ ��������� ������, ������ ������������ ���: 
docker run -it task_w2vf 

3. ����� ������� ���������� ������� � ����� ���
cd root

4. ��������� �������� ������
./run_task.sh

�������� ������ �������� � ���� ���������� ��������� ������:

4.1 ���������� ���������� � ������� Spacy: 
python3 script.py �-in corpus.txt �-out dep.contexts 

4.2 ��������� �������� ���������� (cv) � ������� ���� (wv) �� ����� ���������� dep.contexts ��� ����, ������������� �� ����� 1 ����:
./yoavgo-word2vecf-0d8e19d2f2c6/count_and_filter -train dep.contexts -cvocab cv -wvocab wv -min-count 1 

4.3 ��������:
 ./yoavgo-word2vecf-0d8e19d2f2c6/word2vecf -train dep.contexts -wvocab wv -cvocab cv -output dim200vecs -size 200 -negative 15 -threads 10
�������� -size ������ ������ ��������� �������������. �������� ���������� �� ������ �������� wv � cw. ���������, �� �������� �� dep.contexts � �������, ������������. ������� �������� ������� ���� dim200vecs, ���������� ��������� 200-������ ��������� ������������� ����.

4.4 �������������� ���������� ��������� ������������� � ������ �������� NumPy (��� �������������):
python ./yoavgo-word2vecf-0d8e19d2f2c6/scripts/vecs2nps.py dim200vecs vecs
