import pygame

pygame.init() #초기화 (반드시 필요)

screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Ndo Game") #게임 이름

# FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("E:/python/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
chracter = pygame.image.load("E:/python/pygame_basic/chracter.png")
chracter_size = chracter.get_rect().size #이미지의 크기를 구해옴
chracter_width = chracter_size[0] #캐릭터의 가로크기
chracter_height = chracter_size[1] #캐릭터의 세로크기
chracter_x_pos = (screen_width / 2) - (chracter_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치
chracter_y_pos = screen_height - chracter_height#화면 세로크기 가장 아래에 해당하는 곳에 위치

#이동할 좌표
to_x =0
to_y =0

#이동 속도
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("E:/python/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터의 가로크기
enemy_height = enemy_size[1] #캐릭터의 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = (screen_height /2) - (enemy_height / 2)#화면 세로크기 가장 아래에 해당하는 곳에 위치


#이벤트 루프
running = True #게임이 진행중인가? 
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임수 설정 

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: # 창의 x 버튼을 눌렀을 때(닫히는 이벤트가 나왔는가?)
            running = False #게임이 진행중이 아니다
        
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed 
            elif event.key ==pygame.K_RIGHT: #캐릭터를 오른쪽으로 
                to_x += character_speed
            elif event.key ==pygame.K_UP: #캐릭터를 위로
                to_y -= character_speed
            elif event.key ==pygame.K_DOWN: #캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x =0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y =0

    chracter_x_pos += to_x *dt
    chracter_y_pos += to_y *dt

    #가로 경계값 처리
    if chracter_x_pos <0:
        chracter_x_pos =0
    elif chracter_x_pos > screen_width - chracter_width:
        chracter_x_pos =  screen_width - chracter_width

    #세로 경계값 처리
    if chracter_y_pos <0:
        chracter_y_pos =0
    elif chracter_y_pos > screen_height - chracter_height:
        chracter_y_pos = screen_height - chracter_height

    #충돌 처리를 위한 rect 정보 업데이트

    chracter_rect = chracter.get_rect()
    chracter_rect.left = chracter_x_pos #창 기준으로 왼쪽
    chracter_rect.top = chracter_y_pos #화면상의 캐릭터 상의 위쪽

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos 
    enemy_rect.top = enemy_y_pos 

    # 충돌 체크
    if chracter_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(chracter, (chracter_x_pos, chracter_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기

    pygame.display.update() #게임화면을 다시 그리기

#pygame 종료
pygame.quit()