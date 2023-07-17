# pantry-server

run server using ```flask run```

#### Getting recommendations

<details>
 <summary><code>POST</code> <code><b>/rec</b></code> <code>(recommends recipes, default setting: recommends recipes based on if the recipe has the ingredients in it)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | `only_i`      |  optional | bool   | recipes only contain inputed ingredients |
> | `use_rec`      |  optional | bool   | uses recommendation algorithm to recommend relavant recipes |
> | `n`      |  optional | int   | defines number of recipe recommendations, default n=10  |



##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `text/plain;charset=UTF-8`        | `Successful`                                |