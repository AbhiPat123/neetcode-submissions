class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = "".join([f"{len(str_)}|{str_}" for str_ in strs])
        # print(enc_str)
        return enc_str

    def decode(self, s: str) -> List[str]:
        itr = 0
        dcd_list = []
        while itr < len(s):
            pipe_idx = itr
            while s[pipe_idx] != "|":
                pipe_idx += 1
            length = int(s[itr:pipe_idx])

            word = s[pipe_idx+1:pipe_idx+1+length]

            dcd_list.append(word)
            itr = pipe_idx+1+length
            
        # print(dcd_list)
        return dcd_list
