# Stage 1

## Approach to Priority Inbox

The problem requires us to efficiently maintain the top 'n' most important unread notifications based on a combination of weight and recency. New notifications will continuously come in, so the solution must handle additions dynamically without performance degradation.

### Priority Criteria
1. **Weight**: We assign a numerical weight to the notification type:
   - `Placement`: 3
   - `Result`: 2
   - `Event`: 1
2. **Recency**: When weights are equal, the notification with the newer timestamp takes precedence.

### Data Structure: Min-Heap (Priority Queue)
To efficiently maintain the "top n" notifications, a Min-Heap of size `n` is the optimal choice.

**Why a Min-Heap?**
- A min-heap allows us to keep track of the *smallest* element (the least important notification) at its root in `O(1)` time.
- When the heap reaches size `n`, any new incoming notification is compared against the root. 
- If the new notification is *more important* than the root, we remove the root (`O(log n)`) and insert the new notification (`O(log n)`).
- If it's less important, we simply discard it.

**Sorting Logic in the Heap:**
The heap orders elements such that the *least* important element is at the root. The comparator logic is:
- Element A is "less than" Element B if:
  1. `Weight(A) < Weight(B)`
  2. OR `Weight(A) == Weight(B)` AND `Timestamp(A) < Timestamp(B)` (A is older than B)

### Algorithm Steps
1. Initialize an empty Min-Heap.
2. For each incoming notification:
   - Calculate its priority score.
   - If the heap size is less than `n`, insert the notification.
   - If the heap size equals `n`, compare the notification with the heap's root. If it's strictly greater (higher weight or newer), extract the root and insert the new notification.
3. Once all (or current batch of) notifications are processed, the heap contains the top `n` notifications. 
4. Extract the elements from the heap and reverse them to display from most important to least important.

### Complexity
- **Time Complexity:** For `m` incoming notifications, the time to maintain the top `n` is `O(m log n)`. This is highly efficient and scalable, even for millions of notifications, because `n` is typically small (e.g., 10, 20).
- **Space Complexity:** `O(n)` to store the top `n` elements in memory.

This ensures real-time updates to the Priority Inbox are handled extremely quickly, without requiring a full re-sort or database query upon every insertion.
