<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Стартовая страница</title>
</head>
<body>
Greeting : ${greeting}
<br/>
<h3>Привествуем Вас!!!</h3>

Кликните здесь <a href="<c:url value="/login" />">Перейти к авторизации</a>.
</body>
</html>