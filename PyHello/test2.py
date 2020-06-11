# input num
# ouput chinese

class Solution:

    def covert(self, num):
        chinese_arr = ['零','壹','贰','','','','']
        num_str = str(num)
        left, right = int(num_str.split('.')[0]), int(num_str.split('.')[1][:2])
        res = ''
        # 整数部分
        while(left>9):
            # wan
            if(len(left)>=4):
                res += chinese_arr[left // 10000] + '万'
                left = left % 10000
            elif(len(left)>=3):
                res += chinese_arr[left // 1000] + '千'
                left = left % 1000
            elif (len(left)>=2):
                res += chinese_arr[left // 100] + '百'
                left = left % 100
            elif (len(left)>=1):
                res += chinese_arr[left // 10] + '十'
                left = left % 10
        res += chinese_arr[left]



        return res


test = Solution()
print(test.covert("1.6"))