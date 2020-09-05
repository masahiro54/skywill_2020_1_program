WITH A AS(
SELECT 
   w.lemma
  ,s.synset
  ,w.pos
  ,sd.def
FROM  
    word AS w
INNER JOIN
    sense AS s
ON
  w.wordid = s.wordid
LEFT JOIN
  synset_def AS sd
ON
  sd.synset = s.synset
WHERE w.lang = 'jpn' AND sd.lang = 'jpn'
),

link_j AS (
SELECT synset1,synset2 FROM synlink
where link = 'hypo'
)

-- SELECT 1,lemma,def,
-- FROM synlink sl
-- LEFT JOIN 
--   A
-- ON
--  sl.synset1 = A.synset
-- WHERE synset1 = '14123044-n'
-- union ALL
-- SELECT 2,lemma,def,synset1
-- FROM synlink sl
-- LEFT JOIN 
--   A
-- ON
--  sl.synset2 = A.synset
-- WHERE synset1 = '14123044-n'

--下位概念
SELECT 2,lemma AS kai_name,def,(SELECT lemma FROM A WHERE synset1 = A.synset) AS joui_name
FROM synlink sl
LEFT JOIN 
  A
ON
 sl.synset2 = A.synset
WHERE lemma like '%ネコ%'