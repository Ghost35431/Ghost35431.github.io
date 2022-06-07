import os
import sys
import cmath
import pygame
import math

class consol:
  def echo(temp): os.system("echo " + temp)
  pi = math.pi
  #bash apt install
  def apt(pkg): os.system('apt install ' + pkg)
  def clear(): os.system('clear()')

def test(argsv): echo(args)

def main():
  consol.echo('testing')
