- 파일 내용 보기: cat, more, less
- 파일 숏컷: ln(심볼릭 클릭)
- 파일 속성 보기: file

- 디렉토리 만들기: mkdir, rmdir
- 시스템 종료: reboot, poweroff, shutdown

#### ls
- ls: list
- ls -l: long list
- ls -a: all
- ls -al: all + long
- ls -a-l: all + long
- ls *.txt: 확장자가 *.txt인 것

#### touch
- 한 번에 여러 파일 만들기 가능: ``touch test1 test2 test``

#### cat
- cat -e <file_name>: 줄 맨 뒤에 $ 붙이기(히든 캐릭터 공백 등 확인)
- cat -n <file_name>: 줄 번호 보여주기

#### more
- 파일 내용 보기
- 페이지 단위로 이동: space
- 줄 단위로 이동: Enter
- more <file_name>
 
#### less
- 파일 내용 보기
- 페이지 단위로 이동: space
- 줄 단위로 이동: Enter
- 방향키: 상하좌우, 페이지 up/down
- less <file_name>
- more보다 향상된 기능, 모든 파일을 메모리에 올리지 않아 more대비 고속


#### mkdir
- 여러 디렉토리 생성 가능(`mkdir dir1 dir2`)
- 계층구조 디렉토리 생성 가능(`mkdir -p dir1/sub1`)
  - `rm dir1`실패
  - `rm -p dir1` 성공

#### rmdir


#### cp
- 디렉토리 복사: cp -r <dir_name>

#### ln
- 링크 만들기
- 소프트 링크(심볼릭): ln -s hello.txt hello
- 링크 만들기: ln -hello.txt hello
- 
<img width="949" alt="스크린샷 2021-11-20 오후 2 20 20" src="https://user-images.githubusercontent.com/60768642/142715450-d825b68e-7557-4878-bb3b-e0ddb90aec4b.png">

#### file
- ``file <file_name>``: 파일 속성 보여주는 명령어

#### 시스템 종료
<img width="918" alt="스크린샷 2021-11-20 오후 2 22 41" src="https://user-images.githubusercontent.com/60768642/142715486-a469406f-1db6-435d-be1e-1d31aa6895ce.png">

#### whoami

#### id
- 내 아이디 출력

#### sudo su
- 루트 권한으로 로그인(현재 디렉토리에서)
#### sudo su -
- 루트 권한으로 로그인(홈 디렉토리로 이동)

#### cat /etc/password
- 사용자 계정 확인
 
- <img width="1025" alt="스크린샷 2021-11-20 오후 2 28 29" src="https://user-images.githubusercontent.com/60768642/142715594-5020f956-74b6-457f-8adc-cdca5ba680f6.png">

#### cat /etc/group
- 사용자 그룹 확인

#### chown
<img width="1082" alt="스크린샷 2021-11-20 오후 2 30 55" src="https://user-images.githubusercontent.com/60768642/142715659-2d4ca83d-fd8b-4de0-8a7e-b07e423b3a7f.png">
