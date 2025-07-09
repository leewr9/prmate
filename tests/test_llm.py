import pytest
from app.llm.chains import ReviewChain

def test_review_chain():
    chain = ReviewChain()
    sample_code = """
diff --git a/README b/README
index c57eff55..719be62e 100644
--- a/README
+++ b/README
@@ -1 +1,6 @@
-Hello World!
\\ No newline at end of file
+Hello World!
+$ mkdir ~/Hello-World
+$ cd ~/Hello-World
+$ git init
+Initialized empty Git repository
+$ touch README
\\ No newline at end of file
"""
    review = chain.generate_review(sample_code)
    assert isinstance(review, str)
    assert len(review) > 0
