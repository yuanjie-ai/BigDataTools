<h1 align = "center">:rocket: Pyspark :facepunch:</h1>

---

## Model Save
```python
model.write().overwrite().save(file_path)
```

## 调用python模型
```python
sc.addFile('model')  # 打包必须
udf(lambda x: lr.predict_proba(np.array([[x]]))[:, 1].tolist()[0], FloatType())
```
