class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> stackc;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                stackc.push(s[i]);
            } else {
                if (stackc.empty()) return false;
                if (s[i] == ')' && stackc.top() == '(') {
                    stackc.pop();
                } else if (s[i] == '}' && stackc.top() == '{') {
                    stackc.pop();
                } else if (s[i] == ']' && stackc.top() == '[') {
                    stackc.pop();
                } else {
                    return false;
                }
            }
        }
        return stackc.empty();
    }
};