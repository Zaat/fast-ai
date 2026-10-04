# Rejected attempts

Every attempt below was proposed during the sessions and rejected. Re-run with `tools/run_rejected.py`.
TREE(2) should print 3.

| File | Chars | Why it was tried / what is wrong | gcc warnings | TREE(2) plain | TREE(2) with ASan/UBSan |
|---|---:|---|---:|---|---|
| 01_unsequenced_p_increment.c | 859 | P[p][1]=p++ reads and changes p without a sequence point (undefined); gcc increments first and writes an unallocated slot. | 26 | segmentation fault (0.0s) | heap-buffer-overflow |
| 02_global_c_k_b_in_recursion.c | 790 | Makes c, k, b global in recursive functions; nested calls overwrite the caller's loop state. | 23 | 2 (rc=0, 0.0s) | 2 (rc=0) |
| 03_q_loop_without_empty_body.c | 787 | Same as 02 plus the q loop lost its empty body, so the record step runs inside the loop where q>=0. | 23 | 0 (rc=0, 0.0s) | 0 (rc=0) |
| 04_unparenthesised_abs_macro.c | 767 | #define A(n)n<0?-n:n: i+A(x[i]) parses as (i+x[i]<0)?...; also longer than abs (+17 net in the 761 variant). | 25 | killed (out of memory) | heap-buffer-overflow |
| 05_return_not_i_lt_I.c | 780 | return!i<I parses as (!i)<I, not i>=I (proposed four times). | 28 | 2 (rc=0, 0.0s) | 2 (rc=0) |
| 06_else_return_longer.c | 796 | Correct, but if/else-return inside an endless loop is 16 chars longer. | 27 | 3 (rc=1, 0.0s) | 3 (rc=1) |
| 07_embedding_check_deleted.c | 750 | "751 chars": deletes the embedding check, so q never goes negative and nothing is recorded. | 28 | 0 (rc=0, 0.0s) | 0 (rc=0) |
| 08_pasted_598_claim.c | 795 | Code from an analysis that claimed to be a corrected 598-char version; it is actually 795 chars (works, but the claim and the reported bugs were wrong). | 27 | 3 (rc=0, 0.0s) | 3 (rc=0) |
| 09_abs_macro_p1_shift.c | 771 | Unparenthesised abs macro plus p+1<<3 sizes; same misparse as 04. | 27 | killed (out of memory) | no result in 10 s |
| 10_no_self_check.c | 626 | Removes the self-comparison guard; x and y alias, sign-marking corrupts both trees. | 25 | killed (out of memory) | no result in 10 s |
| 11_no_abs_on_sibling_step.c | 678 | c+=y[c] without abs: a marked (negative) child makes the scan step backwards. TREE(2) happens to print 3, but the 3,000-pair embedding test hangs on pair 4. | 29 | 3 (rc=0, 0.0s) | 3 (rc=0) |
| 12_int_S_pointer_truncation.c | 604 | int*S storing tree pointers truncates them to 32 bits (and drops the self-check); segfault. | 28 | segmentation fault (0.0s) | SEGV |
