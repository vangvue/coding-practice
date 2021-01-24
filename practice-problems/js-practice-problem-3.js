// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
// 559. Maximum Depth of N-ary Tree

// Given a n-ary tree, find its maximum depth.
//
// The maximum depth is the number of nodes along the longest path
// from the root node down to the farthest leaf node.
//
// Nary-Tree input serialization is represented in their level order traversal,
// each group of children is separated by the null value (See examples).

var maxDepth = function(root) {
    let max = 0;
    function traverse(node, depth) {
        if (!node) return;
        if(depth > max) max = depth;
        for(let i = 0; i < node.children.length; i++) {
            traverse(node.children[i], depth + 1); // depth +1 gives updated value
        }
    }
    traverse(root, 1);
    return max;
};
