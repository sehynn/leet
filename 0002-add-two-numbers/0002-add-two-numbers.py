#연결 리스트로 표현된 두 숫자를 더해서 연결리스트로 반환하자 
#------------------------------------------------
#연결 리스트에서 값 뺴오는법: 연결리스트.val
#연결 리스트에서 다음 노드로 가는법 : 연결리스트.next
#연결 리스트 시작 노드 선언 : ListNode()
#신경써야될건 반복문 and 올림값

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode()
        cur=dummy #포인터를 만들어주는거임
        carry=0 #올림값 

        while carry or l1 or l2:
            total=carry
            if l1:
                total+=l1.val
                l1=l1.next
            if l2:
                total+=l2.val
                l2=l2.next
            carry=total//10 #올림값 
            digit=total%10 #남은 일의 자리 수 

            #포인터 값이 일의 자리 수가 되고, 포인터도 넘어가도록
            cur.next=ListNode(digit)
            cur=cur.next 
            
        return dummy.next
                

 

