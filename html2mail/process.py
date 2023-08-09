def process(a):
    b = a
    body = False
    not_adjustment = False
    mail = []
    for idx, line in enumerate(b.split('\n')):
        aux_line = line.strip()
        if 'style=' in aux_line:
            temp_style = aux_line.split('style=')
            temp_style[1] = 'style=' + ' !important;'.join(temp_style[1].split(';'))
            aux_line = ' '.join(temp_style)
        if aux_line.startswith('</body'):
            body = False
        if aux_line.startswith('<body') or body:
            if not body:
                body = True
                mail.append(aux_line)
                continue
            if not aux_line:
                continue
            elif aux_line.startswith('<div'):
                if '</div>' in aux_line:
                    mail.append(aux_line.replace(
                        "<div", '<table cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td').replace(
                        '</div>', '</td></tr></tbody></table>')
                    )
                else:
                    mail.append(
                        aux_line.replace("<div", '<table cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td'))

            elif aux_line.endswith('</div>'):
                mail.append(aux_line.replace('</div>', '</tbody></table>'))
                not_adjustment = False
            elif aux_line.startswith('<span') or aux_line.startswith('<svg') or aux_line.startswith('<a'):
                not_adjustment = True
                mail.append(aux_line)
            elif not_adjustment:
                mail.append(aux_line)
            else:
                if aux_line.startswith('</'):
                    mail.append(aux_line + '</td></tr>')
                else:
                    if '</' in aux_line or aux_line.startswith('<img'):
                        mail.append('<tr><td>' + aux_line + '</td></tr>')
                    elif '<' in aux_line:
                        mail.append('<tr><td>' + aux_line)
                    else:
                        mail.append(aux_line)
        else:
            mail.append(aux_line)
    return mail
