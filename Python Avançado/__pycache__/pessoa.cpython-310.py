o
    w�b�  �                   @   s   d dl m Z  G dd� d�ZdS )�    )�datetimec                   @   sR   e Zd Zee�e�� d��Zddd�Zdd� Z	dd� Z
d	d
� Zdd� Zdd� ZdS )�Pessoaz%YFc                 C   s   || _ || _|| _|| _d S �N)�nome�idade�comendo�falando)�selfr   r   r   r   � r
   �A   /home/higor/Documentos/PrimeiroProjeto/Python Avançado/pessoa.py�__init__   s   
zPessoa.__init__c                 C   sT   | j rt| j� d�� d S | jrt| j� d�� d S t| j� d|� d�� d| _d S )Nu    não pode falar comendo.u    já está falando.u    está falando sobre �.T�r   �printr   r   )r	   Zassuntor
   r
   r   �falar   �   
zPessoa.falarc                 C   �4   | j st| j� d�� d S t| j� d�� d| _ d S )Nu    não está falandoz parou de falar.F)r   r   r   �r	   r
   r
   r   �parar_falar   �
   
zPessoa.parar_falarc                 C   sT   | j rt| j� d�� d S | jrt| j� d�� d S t| j� d|� d�� d| _ d S )Nu    já está comendo.u    não pode comer falando.u    está comendo r   Tr   )r	   Zalimentor
   r
   r   �comer    r   zPessoa.comerc                 C   r   )Nu    não está comendo.z parou de comer.F)r   r   r   r   r
   r
   r   �parar_comer,   r   zPessoa.parar_comerc                 C   s   | j | j S r   )�	ano_atualr   r   r
   r
   r   �get_ano_nascimento4   s   zPessoa.get_ano_nascimentoN)FF)�__name__�
__module__�__qualname__�intr   �strftimeZnowr   r   r   r   r   r   r   r
   r
   r
   r   r      s    
r   N)r   r   r
   r
   r
   r   �<module>   s    