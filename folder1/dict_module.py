#!-*-coding:utf-8-*-
import matplotlib as plt

__all__ = ["lineplot","scatter"]


"""
辞書を効率的に扱う

ある、トータルの概念　＝　クラス


"""
#!-*-coding:utf-8-*-
import matplotlib.pyplot as plt
class lineplot:
    def __init__( self , xlim , ylim , filename ):
        self.xlim = xlim
        self.ylim = ylim
        self.filename = filename

    def plot(self,x , y ):
        plt.grid()
        plt.plot( x , y )
        plt.xlim( self.xlim ) , plt.ylim( self.ylim )
        plt.savefig( self.filename )

class scatter:
    def __init__( self , xlim , ylim , filename ):
        self.xlim = xlim
        self.ylim = ylim
        self.filename = filename
    def plot(self, x , y ):
        plt.grid()
        plt.xlim( self.xlim ) , plt.ylim( self.ylim )
        plt.savefig( self.filename )
