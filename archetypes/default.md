---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }} 
slug: "{{ now.Format "2006-01-02" }}" 
draft: true
tags:
  - monthly
description:
comment: true
toc: true
layout: ""
---