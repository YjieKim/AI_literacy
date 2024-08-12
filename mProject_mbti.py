# 진짜 최종(24.07.24)

import MBTI_food as mbti_fd
import mbti_workout_eunji as mbti_wo
import mbti_movie as mbti_mv

def mbti_main():
  
    # 시작할 때 안내 메시지 출력
    print(f"""
    어느새 벌써 7월 말! 이번 주말 어떤 계획을 가지고 계신가요?
    특별한 계획이 없으시다면, e조에서 당신만을 위한 제안 한 번 드려볼게요.

    MBTI에 맞게 당신만을 위해 준비했으니, 당신의 MBTI를 먼저 입력해주세요~
    """)

    # MBTI 잘못 입력한 경우 개수 세기
    cnt = 0

    while True:
        user_mbti = input("당신의 MBTI를 알려주세요! >> ")  # MBTI 입력받기
        user_mbti = user_mbti.upper()   # 입력한 MBTI를 모두 대문자로 바꾸기

        # MBTI를 제대로 입력했는지 확인
        mbti_list = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
                    "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]

        if user_mbti in mbti_list:

            recommend_food = mbti_fd.re_food(user_mbti)   # 음식 추천
            recommend_workout = mbti_wo.get_random_workout(user_mbti)   # 운동 추천
            recommend_movie, reason = mbti_mv.recommend_movie(user_mbti)    # 영화 추천

            print(f"""
            ************************************************************************

            당신의 MBTI는 {user_mbti}네요.
            그럼 {user_mbti}인 당신만을 위한 추천 드립니다.

            이번 주말에는 {recommend_food}를 드셔보세요.

            (아주 많이) 덥고 습하지만… 운동도 잊으면 안 되죠.
            {recommend_workout}도 한 번 해보세요~

            마지막으로 시원한 맥주와 함께
            '{recommend_movie}' 영화를 보며 주말 마무리를 해 보아요.
            {reason}

            그럼 행복한 주말 보내기를 바랍니다.
            다음 주에도 심심하면 다시 방문해 주세요~

            ************************************************************************
            """)

            break

        else:   # MBTI를 잘못 입력했을 경우
            cnt = cnt + 1

            if cnt >= 3:   # 세 번까지만 반복해서 물어보기
                print(f"{cnt}번 잘못 입력하셨어요. 다음에 다시 찾아주세요.")
                break
            else:
                print("MBTI를 잘못 입력하셨네요. 다시 입력해 주세요.")


if __name__=='__main__':
    mbti_main()