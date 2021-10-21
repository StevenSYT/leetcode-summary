/*
 * @lc app=leetcode id=295 lang=cpp
 *
 * [295] Find Median from Data Stream
 */

// @lc code=start
class MedianFinder {
public:
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if (left.empty() || num <= left.top()) {
            left.push(num);
        } else {
            right.push(num);
        }

        if (left.size() < right.size()) {
            left.push(right.top());
            right.pop();
        } else if (left.size() - right.size() >= 2) {
            right.push(left.top());
            left.pop();
        }
    }
    
    double findMedian() {
        if (left.size() == right.size()) {
            return (static_cast<double>(left.top()) + right.top()) / 2;
        } else {
            return left.top();
        }
    }
private:
    std::priority_queue<int, std::vector<int>, std::less<int>> left; // max-heap
    std::priority_queue<int, std::vector<int>, std::greater<int>> right; // min-heap

};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
// @lc code=end

