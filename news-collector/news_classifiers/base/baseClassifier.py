#coding: utf8


class BaseClassifier(object):
    '''
    分类器基类，所有分类器须继承此类并实现方法
    '''

    def classify(title, **kvargs):
        '''
        输入标题返回该标题的分类
        '''
        raise NotImplementedError('subclasses of BaseClassifier must provide a classify() method')
