import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.mail.MessagingException;

@RestController
@RequestMapping("/auth")
public class AuthController {

    @Autowired
    private UserService userService;

    @Autowired
    private EmailService emailService;

    // 用户注册
    @PostMapping("/register")
    public String register(@RequestParam String email, @RequestParam String password) {
        try {
            userService.registerUser(email, password);
            return "注册成功！";
        } catch (RuntimeException e) {
            return "注册失败: " + e.getMessage();
        }
    }

    // 用户登录
    @PostMapping("/login")
    public String login(@RequestParam String email, @RequestParam String password) {
        boolean authenticated = userService.authenticateUser(email, password);
        if (authenticated) {
            return "登录成功！";
        } else {
            return "登录失败: 邮箱或密码错误";
        }
    }

    // 发送邮箱验证码
    @PostMapping("/sendVerificationCode")
    public String sendVerificationCode(@RequestParam String email) {
        try {
            String verificationCode = emailService.generateEmailVerificationCode();
            emailService.sendEmail(email, "邮箱验证码", "您的验证码是: " + verificationCode);
            return "验证码已发送到邮箱：" + email;
        } catch (MessagingException e) {
            return "发送验证码失败: " + e.getMessage();
        }
    }
}
