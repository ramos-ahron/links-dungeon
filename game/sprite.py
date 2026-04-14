"""Sprite class used for every object in the game (player, enemies, blocks, boss)."""
import pygame

from game.assets import asset_path

WHITE = (255, 255, 255)
class Sprite(pygame.sprite.Sprite):
  #Default Property Variables
  xSpeed = 0 
  ySpeed = 0
  x = 0
  y = 0
  width = 0
  height = 0
  images = []
  index = 0
  time = 0
  #Constructor function. Executes when object is created
  #Can load an image instead of rectangle, default is none
  def __init__(self,width, height, color, image = None):
      # Call the parent class (Sprite) constructor
      super().__init__() 
      self.image = pygame.Surface([width, height])
      if image == None:
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
      else:
        self.image = pygame.image.load(asset_path(image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, [width, height])
        self.images = []
        self.images.append(image)
      #Get rectangle boundaries of object
      self.rect = self.image.get_rect()
      self.width = width
      self.height = height
      
  #Set/Get functions for coordinates
  def setX(self,x):
    self.rect.x = x
    self.x = self.rect.x
  def getX(self):
    return self.rect.x
  def setY(self,y):
    self.rect.y = y
    self.y = self.rect.y
  def getY(self):
    return self.rect.y
  def setPosition(self,x,y):
    self.rect.x = x
    self.rect.y = y
  def getHeight(self):
    return self.height
  def getWidth(self):
    return self.width
  
  #Move object repeatedly across the screen
  def move(self,xSpeed, ySpeed):
    self.rect.x += xSpeed
    self.rect.y += ySpeed
    
  #collision detection functon
  def collision(self, object2):
    if pygame.sprite.collide_rect(self,object2):
      return True
    else:
      return False

  #Add different images to Sprite objects collection
  def addImage(self, image):
    self.images.append(image)
    
  # Go to the next image and add a delay if necessary
  def nextImage(self, delay = None):
      self.time += 1
      if self.index < len(self.images) - 1 and self.time >= delay:
        self.index+=1
        image = self.images[self.index]
        self.image = pygame.image.load(asset_path(image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, [self.width, self.height])
        self.time = 0
      elif self.index >= len(self.images) - 1:
        self.index = 0
        
  #Sets a specific image based on index. First image is 0
  def setImageIndex(self, index):
      self.index = index
      image = self.images[self.index]
      self.image = pygame.image.load(asset_path(image)).convert_alpha()
      self.image = pygame.transform.scale(self.image, [self.width, self.height])
      
  #Creates an animation of the images if in a game loop. Start at an inde and go to a specific index
  #Delay will speed up or slow down the animation
  def imageStartEnd(self, startIndex, endIndex, delay):
      self.time += 1
      if self.index <startIndex or self.index > endIndex:
        self.index = startIndex
      elif startIndex < endIndex and self.time >= delay:
        image = self.images[self.index]
        self.image = pygame.image.load(asset_path(image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, [self.width, self.height])
        self.time = 0
        self.index+=1
      elif self.index > endIndex:
        self.index = 0



      


        
